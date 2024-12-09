import { Character, Class, ClassSpecialization } from "./preloaded";

export class WowServer {
    allPlayers: Character[] = [];

    add(nickname: string, characterClass: Class, spec: ClassSpecialization): void {
      allPlayers.append(Character(nick))
    }

    addMany(...characters: Character[]): void {}

    count(nickname?: string, charClass?: Class, spec?: ClassSpecialization): number {
        return 0;
    }

    exists(nickname?: string, charClass?: Class, spec?: ClassSpecialization): boolean {
        return false;
    }

    find(nickname?: string, charClass?: Class, spec?: ClassSpecialization): Character[] {
        return [];
    }

    getAll(): Character[] {
        return [];
    }

    remove(nickname?: string, charClass?: Class, spec?: ClassSpecialization, count?: number): void {}

    removeFirst(nickname?: string, charClass?: Class, spec?: ClassSpecialization): void {}
}
