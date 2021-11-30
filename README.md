# devops-netology

Добавлен файл terraform/.gitignore в котором содержаться исключения для файлов и кешей Terraform используемых локально:
**/.terraform/* - все директории .terraform и файлы в них независимо от уровная вложенности (abc/.terraform, a/b/c/.terraform/)
*.tfstate - все файлы с расширением .tfstate
*.tfstate.* - все файлы с .tfstate. в названии
crash.log - файл с именем crash.log
*.tfvars - все файлы с расширением .tfvars
override.tf - файл с именем override.tf
override.tf.json - файл с именем override.tf.json
*_override.tf - все файлы заканчивающиеся на _override.tf
*_override.tf.json - все файлы заканчивающиеся на _override.tf.json
.terraformrc - директория или файл с именем .terraformrc
terraform.rc - директория или файл с именем terraform.rc