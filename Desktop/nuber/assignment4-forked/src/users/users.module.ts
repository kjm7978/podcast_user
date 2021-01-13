import { JwtService } from './../jwt/jwt.service';
import { UsersResolver } from './users.resolver';
import { UsersService } from './users.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Module } from '@nestjs/common';
import { User } from './entities/user.entity';

@Module({
    imports : [TypeOrmModule.forFeature([User])],
    providers : [UsersService, UsersResolver],
    exports : [UsersService],
})
export class UsersModule {}
