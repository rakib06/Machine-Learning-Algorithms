```commandline
ERROR: After October 2020 you may experience errors when installing or updating packages. This is because pip will change the way that it resolves dependency conflicts.

We recommend you use --use-feature=2020-resolver to test your packages with the new resolver before it becomes the default.

tensorflow-tensorboard 0.4.0 requires bleach==1.5.0, but you'll have bleach 3.2.1 which is incompatible.
Successfully installed MarkupSafe-1.1.1 Send2Trash-1.5.0 argon2-cffi-20.1.0 async-generator-1.10 attrs-20.3.0 backcall-0.2.0 bleach-3.2.1 cached-property-1.5.2 cffi-1.14.3 colorama-0.4.4 decorator-4.4.2 defusedxml-0.6.0 entrypoints-0.3 enum34-1.1.10 h5py-3.1.0 html5lib-0.9999999 importlib-metadata-2.0.0 ipykernel-5.3.4 ipython-7.16.1 ipython-genutils-0.2.0 ipywidgets-7.5.1 jedi-0.17.2 jinja2-2.11.2 jsonschema-3.2.0 jupyter-1.0.0 jupyter-client-6.1.7 jupyter-console-6.2.0 jupyter-core-4.7.0 jupyterlab-pygments-0.1.2 keras-2.4.3 markdown-3.3.3 mistune-0.8.4 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.0.8 nest-asyncio-1.4.3 notebook-6.1.5 numpy-1.19.4 packaging-20.4 pandocfilters-1.4.3 parso-0.7.1 pickleshare-0.7.5 prometheus-client-0.9.0 prompt-toolkit-3.0.8 protobuf-3.14.0 pycparser-2.20 pygments-2.7.2 pyparsing-2.4.7 pyrsistent-0.17.3 python-dateutil-2.8.1 pywin32-300 pywinpty-0.5.7 pyyaml-5.3.1 pyzmq-20.0.0 qtconsole-4.7.7 qtpy-1.9.0 scipy-1.5.4 six-1.15.0 tensorflow-1.4.0 tensorflow-tensorboard-0.4.0 terminado-0.9.1 testpath-0.4.4 tornado-6.1 traitlets-4.3.3 wcwidth-0.2.5 webencodings-0.5.1 werkzeug-1.0.1 widgetsnbextension-3.5.1 zipp-3.4.0

# Solutiion:
(ml_venv) C:\venvs\ml_venv>
    pip install jupyter notebook tensorflow==1.4 keras --use-feature=2020-resolver
```