"""
containers.py — Dependency Injection via dependency-injector.
"""

from dependency_injector import containers, providers


class RepositoryContainer(containers.DeclarativeContainer):
    """Container de repositórios MongoDB."""

    # mongodb_client = providers.Singleton(...)
    # example_repository = providers.Singleton(MongoDBExampleRepository, client=mongodb_client)


class UseCaseContainer(containers.DeclarativeContainer):
    """Container de use cases."""

    repository = providers.DependenciesContainer()

    # example_use_case = providers.Singleton(
    #     ExampleUseCase,
    #     repository=repository.example_repository,
    # )


class ApplicationContainer(containers.DeclarativeContainer):
    """Container raiz da aplicação."""

    repository = providers.Container(RepositoryContainer)
    use_case = providers.Container(UseCaseContainer, repository=repository)


container = ApplicationContainer()
