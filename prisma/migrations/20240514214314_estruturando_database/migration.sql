-- CreateTable
CREATE TABLE "Aviao" (
    "id" SERIAL NOT NULL,
    "modelo" TEXT NOT NULL,

    CONSTRAINT "Aviao_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Passageiro" (
    "cpf" TEXT NOT NULL,
    "Nome" TEXT NOT NULL,

    CONSTRAINT "Passageiro_pkey" PRIMARY KEY ("cpf")
);

-- CreateTable
CREATE TABLE "Funcionario" (
    "cpf" TEXT NOT NULL,
    "Nome" TEXT NOT NULL,
    "cargo" TEXT NOT NULL,
    "fk_Aviao_id" INTEGER NOT NULL,

    CONSTRAINT "Funcionario_pkey" PRIMARY KEY ("cpf")
);

-- CreateTable
CREATE TABLE "Destinos" (
    "id" SERIAL NOT NULL,
    "local" TEXT NOT NULL,

    CONSTRAINT "Destinos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Voo" (
    "id" SERIAL NOT NULL,
    "fk_Destinos_id" INTEGER NOT NULL,
    "fk_Aviao_id" INTEGER NOT NULL,

    CONSTRAINT "Voo_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Reserva" (
    "fk_voo_id" INTEGER NOT NULL,
    "fk_passageiro_cpf" TEXT NOT NULL,

    CONSTRAINT "Reserva_pkey" PRIMARY KEY ("fk_voo_id","fk_passageiro_cpf")
);

-- CreateIndex
CREATE UNIQUE INDEX "Destinos_local_id_key" ON "Destinos"("local", "id");

-- AddForeignKey
ALTER TABLE "Funcionario" ADD CONSTRAINT "Funcionario_fk_Aviao_id_fkey" FOREIGN KEY ("fk_Aviao_id") REFERENCES "Aviao"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Voo" ADD CONSTRAINT "Voo_fk_Destinos_id_fkey" FOREIGN KEY ("fk_Destinos_id") REFERENCES "Destinos"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Voo" ADD CONSTRAINT "Voo_fk_Aviao_id_fkey" FOREIGN KEY ("fk_Aviao_id") REFERENCES "Aviao"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Reserva" ADD CONSTRAINT "Reserva_fk_voo_id_fkey" FOREIGN KEY ("fk_voo_id") REFERENCES "Voo"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Reserva" ADD CONSTRAINT "Reserva_fk_passageiro_cpf_fkey" FOREIGN KEY ("fk_passageiro_cpf") REFERENCES "Passageiro"("cpf") ON DELETE RESTRICT ON UPDATE CASCADE;
