# Generated by Django 2.2.28 on 2024-05-10 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0075_auto_20240429_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='annotation_classification',
            field=models.BooleanField(default=False, help_text='If these annotations are suitable for training a general purpose model. If in doubt uncheck this.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='annotation_guideline_link',
            field=models.TextField(blank=True, default='', help_text='link to an external document (i.e. GoogleDoc, MS Sharepoint)outlining a guide for annotators to follow for this project,an example is available here: https://docs.google.com/document/d/1xxelBOYbyVzJ7vLlztP2q1Kw9F5Vr1pRwblgrXPS7QM/edit?usp=sharing'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cuis',
            field=models.TextField(blank=True, default=None, help_text='A list of comma seperated concept unique identifiers (CUIs) to be annotated'),
        ),
        migrations.AlterField(
            model_name='project',
            name='dataset',
            field=models.ForeignKey(help_text='The dataset to be annotated.', on_delete=django.db.models.deletion.CASCADE, to='api.Dataset'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', help_text='A short description of the annotations to be collected and why'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(help_text='The list users that have access to this annotation project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='A name of the annotation project', max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_locked',
            field=models.BooleanField(default=False, help_text='Locked indicates annotation collection is complete and this dataset should not be touched any further.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('A', 'Annotating'), ('D', 'Discontinued (Fail)'), ('C', 'Complete')], default='A', help_text='The status of the annotation collection exercise', max_length=1),
        ),
        migrations.AlterField(
            model_name='projectannotateentities',
            name='concept_db',
            field=models.ForeignKey(help_text='The MedCAT CDB used to annotate / validate', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ConceptDB'),
        ),
        migrations.AlterField(
            model_name='projectannotateentities',
            name='tasks',
            field=models.ManyToManyField(blank=True, default=None, help_text='The set of MetaAnnotation tasks configured for this project', to='api.MetaTask'),
        ),
        migrations.AlterField(
            model_name='projectannotateentities',
            name='vocab',
            field=models.ForeignKey(help_text='The MedCAT Vocab used to annotate / validate', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Vocabulary'),
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name of the annotation project', max_length=150)),
                ('description', models.TextField(blank=True, default='', help_text='A short description of the annotations to be collected and why')),
                ('annotation_guideline_link', models.TextField(blank=True, default='', help_text='link to an external document (i.e. GoogleDoc, MS Sharepoint)outlining a guide for annotators to follow for this project,an example is available here: https://docs.google.com/document/d/1xxelBOYbyVzJ7vLlztP2q1Kw9F5Vr1pRwblgrXPS7QM/edit?usp=sharing')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('cuis', models.TextField(blank=True, default=None, help_text='A list of comma seperated concept unique identifiers (CUIs) to be annotated')),
                ('cuis_file', models.FileField(blank=True, help_text='A file containing a JSON formatted list of CUI code strings, i.e. ["1234567","7654321"]', null=True, upload_to='')),
                ('annotation_classification', models.BooleanField(default=False, help_text='If these annotations are suitable for training a general purpose model. If in doubt uncheck this.')),
                ('project_locked', models.BooleanField(default=False, help_text='Locked indicates annotation collection is complete and this dataset should not be touched any further.')),
                ('project_status', models.CharField(choices=[('A', 'Annotating'), ('D', 'Discontinued (Fail)'), ('C', 'Complete')], default='A', help_text='The status of the annotation collection exercise', max_length=1)),
                ('require_entity_validation', models.BooleanField(default=True, help_text='Entities appear grey and are required to be validated before submission')),
                ('train_model_on_submit', models.BooleanField(default=True, help_text='Active learning - configured CDB is trained on each submit')),
                ('add_new_entities', models.BooleanField(default=False, help_text='Allow the creation of new terms to be added to the CDB')),
                ('restrict_concept_lookup', models.BooleanField(default=False, help_text='Users can only search for concept terms from the list configured for the project, i.e. either from the cuis or cuis_file lists. Checking this when bothcuis and cuis_file are empty does nothing. If "add new entities" is available & added, and cuis or cuis_fileis non-empty the new CUI will be added.')),
                ('terminate_available', models.BooleanField(default=True, help_text='Enable the option to terminate concepts.')),
                ('irrelevant_available', models.BooleanField(default=False, help_text='Enable the option to add the irrelevant button.')),
                ('enable_entity_annotation_comments', models.BooleanField(default=False, help_text='Enable to allow annotators to leave comments for each annotation')),
                ('administrators', models.ManyToManyField(help_text='The set of users that will have visibility of all projects in this project group', related_name='administrators', to=settings.AUTH_USER_MODEL)),
                ('annotators', models.ManyToManyField(help_text='The set of users that will each be provided an annotation project', related_name='annotators', to=settings.AUTH_USER_MODEL)),
                ('cdb_search_filter', models.ManyToManyField(blank=True, default=None, help_text='The CDB that will be used for concept lookup. This specific CDB should have been "imported" via the CDB admin screen', related_name='project_group_concept_source', to='api.ConceptDB')),
                ('concept_db', models.ForeignKey(help_text='The MedCAT CDB used to annotate / validate', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ConceptDB')),
                ('dataset', models.ForeignKey(help_text='The dataset to be annotated.', on_delete=django.db.models.deletion.CASCADE, to='api.Dataset')),
                ('relations', models.ManyToManyField(blank=True, default=None, help_text='Relations that will be available for this project', to='api.Relation')),
                ('tasks', models.ManyToManyField(blank=True, default=None, help_text='The set of MetaAnnotation tasks configured for this project', to='api.MetaTask')),
                ('vocab', models.ForeignKey(help_text='The MedCAT Vocab used to annotate / validate', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Vocabulary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ForeignKey(blank=True, help_text='The annotation project group that this project is part of', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ProjectGroup'),
        ),
    ]