from api.v1.mappers.comment.dto_to_scheme import CommentDTOToSchemeMapper
from api.v1.mappers.user.dto_to_scheme import UserDTOToSchemeMapper
from api.v1.schemes.article.read import ArticleReadScheme, ArticleListScheme
from api.v1.schemes.comment.read import CommentReadScheme
from application.dto.article.article_read import ArticleReadDTO, ArticleListDTO


class ArticleDTOToSchemeMapper:
    @staticmethod
    def to_read_scheme(dto: ArticleReadDTO) -> ArticleReadScheme:
        author_scheme = UserDTOToSchemeMapper.to_list_scheme(dto=dto.author)
        comment_schemes: list[CommentReadScheme] = []
        for comment_dto in dto.comments:
            scheme = CommentDTOToSchemeMapper.to_read_scheme(dto=comment_dto)
            comment_schemes.append(scheme)

        return ArticleReadScheme(
            id=dto.id,
            title=dto.title.value,
            body=dto.body.value,
            status=dto.status,
            created_at=dto.created_at,
            updated_at=dto.updated_at,
            author=author_scheme,
            comments=comment_schemes,
        )

    @staticmethod
    def to_list_scheme(dtos: list[ArticleListDTO]) -> list[ArticleListScheme]:
        schemes = []
        if dtos is None:
            return []
        for dto in dtos:
            if dto is None:
                break
            author_scheme = UserDTOToSchemeMapper.to_list_scheme(dto=dto.author)
            scheme = ArticleListScheme(
                id=dto.id,
                title=dto.title.value,
                status=dto.status,
                author=author_scheme,
                created_at=dto.created_at,
                updated_at=dto.updated_at,
            )
            schemes.append(scheme)
        return schemes
