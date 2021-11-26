package com.sparta.weeklytestspring.domain;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.sparta.weeklytestspring.dto.ArticleCommentRequestDto;
import com.sparta.weeklytestspring.dto.ArticleRequestDto;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@NoArgsConstructor
@Setter
@Getter
@Entity
public class tag extends Timestamped {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    private Long tag;

    @JsonIgnore
    @ManyToOne
    @JoinColumn(name="article_idx", nullable = false)
    private Article article;

    public tag(Long tag, Article article) {
        this.tag = tag;
        this.article = article;
    }
}

