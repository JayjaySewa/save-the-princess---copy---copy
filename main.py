namespace SpriteKind {
    export const enemyShooter = SpriteKind.create()
    export const crusher = SpriteKind.create()
    export const Boss1 = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (number_of_jumps < max_jumps) {
        number_of_jumps += 1
        hero.vy = -70
        hero.fx = 100
    }
})
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
    if (hero.isHittingTile(CollisionDirection.Bottom)) {
        number_of_jumps = 0
    }
    if (hero.tileKindAt(TileDirection.Bottom, assets.tile`myTile6`)) {
        tiles.placeOnTile(hero, tiles.getTileLocation(0, 16))
        info.changeLifeBy(-1)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile10`, function (sprite5, location3) {
    info.changeScoreBy(1)
    tiles.setTileAt(location3, assets.tile`transparency16`)
})
function animateIdle () {
    mainIdleLeft = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainIdleLeft)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d d d d d d d d d e e d f . 
        . f d d f d d d d f d d e d f . 
        . f d d f d d d d f d d d e f . 
        . f d d f d d d d f d d d f . . 
        . f d d d d d d d d d d d f . . 
        . f a c c c c c c c c a b f . . 
        . f d d c c c c c c d d d f . . 
        . f d f f f b b f f f d d f . . 
        . . f a a a a a a a a a b f . . 
        . . . f a a b f f a a b f . . . 
        . . . f a a b f f a a b f . . . 
        . . . . f f f f f f f f . . . . 
        `)
    mainIdleRight = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainIdleRight)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d e e d d d d d d d d d f . 
        . f d e d d f d d d d f d d f . 
        . f e d d d f d d d d f d d f . 
        . . f d d d f d d d d f d d f . 
        . . f d d d d d d d d d d d f . 
        . . f b a c c c c c c c c a f . 
        . . f d d d c c c c c c d d f . 
        . . f d d f f f b b f f f d f . 
        . . f b a a a a a a a a a f . . 
        . . . f b a a f f b a a f . . . 
        . . . f b a a f f b a a f . . . 
        . . . . f f f . . f f f . . . . 
        `)
}
function creatCrusher () {
    crusher2 = sprites.create(img`
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        `, SpriteKind.crusher)
    crusher2.vy = 300
    crusher2.setBounceOnWall(true)
    tiles.placeOnTile(crusher2, tiles.getTileLocation(40, 24))
    crusher2 = sprites.create(img`
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        `, SpriteKind.crusher)
    crusher2.vy = 100
    crusher2.setBounceOnWall(true)
    tiles.placeOnTile(crusher2, tiles.getTileLocation(43, 27))
    crusher2 = sprites.create(img`
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffeeeeeffeeeeeffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        ffffffffffffffffffff
        `, SpriteKind.crusher)
    crusher2.vy = 200
    crusher2.setBounceOnWall(true)
    tiles.placeOnTile(crusher2, tiles.getTileLocation(23, 27))
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile13`, function (sprite2, location2) {
    level += 1
    if (level == 2) {
        tiles.setCurrentTilemap(tilemap`level14`)
        tiles.placeOnTile(hero, tiles.getTileLocation(0, 17))
    } else if (level == 3) {
        tiles.setCurrentTilemap(tilemap`level7`)
        tiles.placeOnTile(hero, tiles.getTileLocation(0, 17))
        spawnEnemy()
    } else if (level == 4) {
        tiles.placeOnTile(hero, tiles.getTileLocation(15, 17))
        sprites.destroyAllSpritesOfKind(SpriteKind.crusher)
        createBossFight()
        sprites.destroy(enemyProjectile)
        game.showLongText("BOSS FIGHT", DialogLayout.Full)
        tiles.setCurrentTilemap(tilemap`level23`)
        info.setLife(4)
        pause(10000)
    }
})
function animateRun () {
    mainRunLeft = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainRunLeft)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f . . . . . . 
        . . f e e e e e e e f . . . . . 
        . f e e e e e e e e e f . . . . 
        . f d d d d e d d e e f . . . . 
        . f d d f d d e d e e f . . . . 
        . f d d f d d d e e e f . . . . 
        . f d d f d d d d d d f . . . . 
        . f d d d d d d d d d f . . . . 
        . . f c c c a a c c b f . . . . 
        . . f c c d d d c c b f . . . . 
        . . f b f f d d f f f f . . . . 
        . . f a a a a a a a b f . . . . 
        . . . f a a a a b f f . . . . . 
        . . . f a a a a b f . . . . . . 
        . . . . f f f f f . . . . . . . 
        `)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f . . . . . . 
        . . f f f f f f f f f . . . . . 
        . f f e e e e e e e f f . . . . 
        . f e e e e e e e e e f . . . . 
        . f d d d d e d d e e f . . . . 
        . f d d f d d e d e e f . . . . 
        . f d d f d d d e e e f . . . . 
        . f d d f d d d d d d f . . . . 
        . f d d d d d d d d d f . . . . 
        . . f c c c c a a c b f . . . . 
        . . f c c c c d d c b f . . . . 
        . . f b f f d d d f f f f . . . 
        . . f a a a a a a a a b f f . . 
        . . . f a a b f f a a a f f . . 
        . . . . f f f f f f f f f . . . 
        `)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f . . . . . . 
        . . f e e e e e e e f . . . . . 
        . f e e e e e e e e e f . . . . 
        . f d d d d e d d e e f . . . . 
        . f d d f d d e d e e f . . . . 
        . f d d f d d d e e e f . . . . 
        . f d d f d d d d d d f . . . . 
        . f d d d d d d d d d f . . . . 
        . . f c c c a a c c b f . . . . 
        . . f c c d d d c c b f . . . . 
        . . f b f f d d f f f f . . . . 
        . . f a a a a a a a b f . . . . 
        . . . f a a a a b f f . . . . . 
        . . . f a a a a b f . . . . . . 
        . . . . f f f f f . . . . . . . 
        `)
    mainRunLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f . . . . . . 
        . . f f f f f f f f f . . . . . 
        . f f e e e e e e e f f . . . . 
        . f e e e e e e e e e f . . . . 
        . f d d d d e d d e e f . . . . 
        . f d d f d d e d e e f . . . . 
        . f d d f d d d e e e f . . . . 
        . f d d f d d d d d d f . . . . 
        . f d d d d d d d d d f . . . . 
        . . f c a a c c c c b f . . . . 
        . f d d d b c c c c b f . . . . 
        f f f d d f f f f f f f . . . . 
        f f f a a a a a a a b f . . . . 
        . f a a b f a a b f f . . . . . 
        . f f f f f f f f . . . . . . . 
        `)
    mainRunRight = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainRunRight)
    mainRunRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f f . . . 
        . . . . . f e e e e e e e f . . 
        . . . . f e e e e e e e e e f . 
        . . . . f e e d d e d d d d f . 
        . . . . f e e d e d d f d d f . 
        . . . . f e e e d d d f d d f . 
        . . . . f d d d d d d f d d f . 
        . . . . f d d d d d d d d d f . 
        . . . . f b c c a a c c c f . . 
        . . . . f b c c d d d c c f . . 
        . . . . f f f f d d f f b f . . 
        . . . . f b a a a a a a a f . . 
        . . . . . f f b a a a a f . . . 
        . . . . . . f b a a a a f . . . 
        . . . . . . . f f f f f . . . . 
        `)
    mainRunRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f f . . . 
        . . . . . f f f f f f f f f . . 
        . . . . f f e e e e e e e f f . 
        . . . . f e e e e e e e e e f . 
        . . . . f e e d d e d d d d f . 
        . . . . f e e d e d d f d d f . 
        . . . . f e e e d d d f d d f . 
        . . . . f d d d d d d f d d f . 
        . . . . f d d d d d d d d d f . 
        . . . . f b c a a c c c c f . . 
        . . . . f b c d d c c c c f . . 
        . . . f f f f d d d f f b f . . 
        . . f f b a a a a a a a a f . . 
        . . f f a a a f f b a a f . . . 
        . . . f f f f f f f f f . . . . 
        `)
    mainRunRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f f . . . 
        . . . . . f e e e e e e e f . . 
        . . . . f e e e e e e e e e f . 
        . . . . f e e d d e d d d d f . 
        . . . . f e e d e d d f d d f . 
        . . . . f e e e d d d f d d f . 
        . . . . f d d d d d d f d d f . 
        . . . . f d d d d d d d d d f . 
        . . . . f b c c a a c c c f . . 
        . . . . f b c c d d d c c f . . 
        . . . . f f f f d d f f b f . . 
        . . . . f b a a a a a a a f . . 
        . . . . . f f b a a a a f . . . 
        . . . . . . f b a a a a f . . . 
        . . . . . . . f f f f f . . . . 
        `)
    mainRunRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f f f . . . 
        . . . . . f f f f f f f f f . . 
        . . . . f f e e e e e e e f f . 
        . . . . f e e e e e e e e e f . 
        . . . . f e e d d e d d d d f . 
        . . . . f e e d e d d f d d f . 
        . . . . f e e e d d d f d d f . 
        . . . . f d d d d d d f d d f . 
        . . . . f d d d d d d d d d f . 
        . . . . f b c c c c a a c f . . 
        . . . . f b c c c c b d d d f . 
        . . . . f f f f f f f d d f f f 
        . . . . f b a a a a a a a f f f 
        . . . . . f f b a a f b a a f . 
        . . . . . . . f f f f f f f . . 
        `)
}
function animateJumps () {
    mainJumpLeft = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainJumpLeft)
    mainJumpLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d d d d d d d d d e e d f . 
        . f d d f d d d d f d d e d f . 
        . f d d f d d d d f d d d e f . 
        . f d d f d d d d f d d d f . . 
        . f d d d d d d d d d d d f . . 
        . f a c c c c c c c c a b f . . 
        . f d d c c c c c c d d d f . . 
        . f d f f f b b f f f d d f . . 
        . . f a a a a a a a a a b f . . 
        . . . f a a b f f a a b f . . . 
        . . . f a a b f f a a b f . . . 
        . . . . f f f . . f f f . . . . 
        `)
    mainJumpLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d d d d d d d d d e e d f . 
        . f d d f d d d d f d d e d f . 
        . f d d f d d d d f d d d e f . 
        . f d d f d d d d f d d d f . . 
        . f d d d d d d d d d d d f . . 
        . f a c c c c c c c c a b f . . 
        . f d d c c c c c c d d d f . . 
        . f d f f f b b f f f d d f . . 
        . . f a a a a a a a a a b f . . 
        . . . f a a b f f a a b f . . . 
        . . . . f f f . . f f f . . . . 
        . . . . . . . . . . . . . . . . 
        `)
    for (let index = 0; index < 30; index++) {
        mainJumpLeft.addAnimationFrame(img`
            . . . . . . . . . . . . . . . . 
            . . . f f f f f f f f f f . . . 
            . . f e e e e e e e e e e f . . 
            . f e e e e e e e e e e e e f . 
            . f d d d d d d d d d e e d f . 
            . f d d f d d d d f d d e d f . 
            . f d d f d d d d f d d d e f . 
            . f d d f d d d d f d d d f . . 
            . f d d d d d d d d d d d f f . 
            . d a b c c c c c c c c b a d . 
            . d a c c c c c c c c c c a d . 
            . f f f f f b b f f f f f f f . 
            . . f a a a a a a a a a b f . . 
            . . . f a a b f f a a b f . . . 
            . . . . f f f . . f f f . . . . 
            . . . . . . . . . . . . . . . . 
            `)
    }
    mainJumpRight = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainJumpRight)
    mainJumpRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d e e d d d d d d d d d f . 
        . f d e d d f d d d d f d d f . 
        . f e d d d f d d d d f d d f . 
        . . f d d d f d d d d f d d f . 
        . . f d d d d d d d d d d d f . 
        . . f b a c c c c c c c c a f . 
        . . f d d d c c c c c c d d f . 
        . . f d d f f f b b f f f d f . 
        . . f b a a a a a a a a a f . . 
        . . . f b a a f f b a a f . . . 
        . . . f b a a f f b a a f . . . 
        . . . . f f f f f f f f . . . . 
        `)
    mainJumpRight.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d e e d d d d d d d d d f . 
        . f d e d d f d d d d f d d f . 
        . f e d d d f d d d d f d d f . 
        . . f d d d f d d d d f d d f . 
        . . f d d d d d d d d d d d f . 
        . . f b a c c c c c c c c a f . 
        . . f d d d c c c c c c d d f . 
        . . f d d f f f b b f f f d f . 
        . . f b a a a a a a a a a f . . 
        . . f f b a a f f b a a f f . . 
        . . f f f f f f f f f f f . . . 
        . . . f f f f f f f f f . . . . 
        `)
    for (let index = 0; index < 30; index++) {
        mainJumpRight.addAnimationFrame(img`
            . . . . . . . . . . . . . . . . 
            . . . f f f f f f f f f f . . . 
            . . f e e e e e e e e e e f . . 
            . f e e e e e e e e e e e e f . 
            . f d e e d d d d d d d d d f . 
            . f d e d d f d d d d f d d f . 
            . f e d d d f d d d d f d d f . 
            . f f d d d f d d d d f d d f . 
            . f f d d d d d d d d d d d f . 
            . d a b c c c c c c c c b a d . 
            . d a c c c c c c c c c c a d . 
            . f f f f f f f b b f f f f f . 
            . . f b a a a a a a a a a f . . 
            . . . f b a a f f b a a f . . . 
            . . . . f f f . . f f f . . . . 
            . . . . . . . . . . . . . . . . 
            `)
    }
}
function animateCrouch () {
    mainCrouchLeft = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainCrouchLeft)
    mainCrouchLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d d d d d d d d d e e d f . 
        . f d d f d d d d f d d e d f . 
        . f d d f d d d d f d d d e f . 
        . f d d f d d d d f d d d f . . 
        . f d d d d d d d d d d d f . . 
        . f a c c c c c c c c a b f . . 
        . f d c c c c c c c c c d d f . 
        f d d f f f b b f f f f d d f . 
        . f f a a a a a a a a a b f . . 
        . . . f f f f . f f f f f . . . 
        `)
    mainCrouchRight = animation.createAnimation(ActionKind.Walking, 100)
    animation.attachAnimation(hero, mainCrouchRight)
    mainCrouchLeft.addAnimationFrame(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . f f f f f f f f f f . . . 
        . . f e e e e e e e e e e f . . 
        . f e e e e e e e e e e e e f . 
        . f d e e d d d d d d d d d f . 
        . f d e d d f d d d d f d d f . 
        . f e d d d f d d d d f d d f . 
        . . f d d d f d d d d f d d f . 
        . . f d d d d d d d d d d d f . 
        . . f b a c c c c c c c c a f . 
        . f d d c c c c c c c c c d f . 
        . f d d f f f f b b f f f d d f 
        . . f b a a a a a a a a a f f . 
        . . . f f f f f . f f f f . . . 
        `)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite3, otherSprite) {
    sprites.destroy(projectile)
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile11`, function (sprite7, location4) {
	
})
function initializeHeroAnimations () {
    animateRun()
    animateJumps()
    animateCrouch()
    animateIdle()
}
function spawnEnemy () {
    enemyProjectile = sprites.create(img`
        ...............ff.......
        .............ff2ffff....
        ............ff2feeeeff..
        ...........ff22feeeeeff.
        ...........feeeeffeeeef.
        ..........fe2222eefffff.
        ..........f2effff222efff
        ..........fffeeeffffffff
        ..........fee44fbe44efef
        ...........feddfb4d4eef.
        ..........c.eeddd4eeef..
        ....ccccccceddee2222f...
        .....dddddcedd44e444f...
        ......ccccc.eeeefffff...
        ..........c...ffffffff..
        ...............ff..fff..
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        `, SpriteKind.enemyShooter)
    tiles.placeOnTile(enemyProjectile, tiles.getTileLocation(27, 7))
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss1, function (sprite6, otherSprite3) {
    hero.x += -10
    info.changeLifeBy(-1)
    for (let index = 0; index < 4; index++) {
        hero.setFlag(SpriteFlag.Invisible, true)
        pause(100)
        hero.setFlag(SpriteFlag.Invisible, false)
        pause(100)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.crusher, function (sprite4, otherSprite2) {
    hero.x += -10
    info.changeLifeBy(-1)
    for (let index = 0; index < 4; index++) {
        hero.setFlag(SpriteFlag.Invisible, true)
        pause(100)
        hero.setFlag(SpriteFlag.Invisible, false)
        pause(100)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite8, otherSprite4) {
    hero.x += -10
    info.changeLifeBy(-1)
    for (let index = 0; index < 4; index++) {
        hero.setFlag(SpriteFlag.Invisible, true)
        pause(100)
        hero.setFlag(SpriteFlag.Invisible, false)
        pause(100)
    }
})
function createBossFight () {
    bossNumber1 = sprites.create(img`
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffeeeeeefffeeeeeefffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        fffffffffffffffffffffffff
        `, SpriteKind.Boss1)
    bossNumber1.vy = 150
    bossNumber1.vx = 100
    bossNumber1.setBounceOnWall(true)
    tiles.placeOnTile(bossNumber1, tiles.getTileLocation(15, 12))
    info.setLife(5)
}
let invincible = 0
let bossNumber1: Sprite = null
let projectile: Sprite = null
let mainCrouchRight: animation.Animation = null
let mainCrouchLeft: animation.Animation = null
let mainJumpRight: animation.Animation = null
let mainJumpLeft: animation.Animation = null
let mainRunRight: animation.Animation = null
let enemyProjectile: Sprite = null
let crusher2: Sprite = null
let mainIdleRight: animation.Animation = null
let mainRunLeft: animation.Animation = null
let mainIdleLeft: animation.Animation = null
let max_jumps = 0
let number_of_jumps = 0
let level = 0
let hero: Sprite = null
scene.setBackgroundColor(9)
tiles.setCurrentTilemap(tilemap`level0`)
game.showLongText("Collect all the coins and save the princess, you will have some challenges along the way", DialogLayout.Full)
creatCrusher()
hero = sprites.create(img`
    . . . . . . f f f f . . . . . . 
    . . . f f f f f f f f f f . . . 
    . . f e e e e e e e e e e f . . 
    . f e e e e e e e e e e e e f . 
    . f d e e d d d d d d d d d f . 
    . f d e d d f d d d d f d d f . 
    . f e d d d f d d d d f d d f . 
    . f f d d d f d d d d f d d f . 
    . f f d d d d d d d d d d d f . 
    . . f b a c c c c c c c c a f . 
    . . f d d d c c c c c c d d f . 
    . . f d d f f f b b f f f d f . 
    . . f b a a a a a a a a a f . . 
    . . . f b a a f f b a a f . . . 
    . . . f b a a f f b a a f . . . 
    . . . . f f f . . f f f . . . . 
    `, SpriteKind.Player)
controller.moveSprite(hero, 100, 0)
scene.cameraFollowSprite(hero)
tiles.placeOnTile(hero, tiles.getTileLocation(0, 16))
hero.ay = 100
initializeHeroAnimations()
info.setLife(3)
level = 1
number_of_jumps = 0
max_jumps = 2
forever(function () {
    if (invincible == 0 && hero.tileKindAt(TileDirection.Center, assets.tile`myTile5`)) {
        invincible = 1
        info.changeLifeBy(-1)
        for (let index = 0; index < 4; index++) {
            hero.setFlag(SpriteFlag.Invisible, true)
            pause(100)
            hero.setFlag(SpriteFlag.Invisible, false)
            pause(100)
        }
        invincible = 0
    }
})
forever(function () {
    for (let value of sprites.allOfKind(SpriteKind.enemyShooter)) {
        pause(1000)
        projectile = sprites.createProjectileFromSprite(assets.image`Sword`, value, -100, -5)
    }
})
forever(function () {
    for (let value2 of tiles.getTilesByType(assets.tile`myTile4`)) {
        tiles.setTileAt(value2, assets.tile`myTile5`)
    }
    pause(1000)
    for (let value3 of tiles.getTilesByType(assets.tile`myTile5`)) {
        tiles.setTileAt(value3, assets.tile`myTile4`)
    }
    pause(1000)
})
