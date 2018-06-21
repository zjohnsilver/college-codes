#Programa que calcula o fatorial de um Numero

fat = 1

x = gets.to_i

for i in 1..x
	fat=fat*i
end
puts "#{x}! = #{fat}"