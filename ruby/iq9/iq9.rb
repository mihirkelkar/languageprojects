class Node
  attr_accessor :prev, :next, :child, :value
  def initialize(value)
    
    @prev = nil
    @next = nil
    @child = nil
    @value = value
  end

  def addchild(value)
    @child = Node.new(value)
  end
end

class Multileveldll
  attr_accessor :head, :tail
  def initialize()
    @head = nil
    @tail = nil		
  end

  def addnode(value, cur = nil)
    if cur == nil
      cur = @tail     
    end
    if cur == nil
      @head = Node.new(value)
      @tail = @head  
    elsif cur != nil
      if cur == @tail
        @tail.next = Node.new(value)
        @tail.next.prev = @tail
        @tail = @tail.next
      elsif cur != @tail
        cur.next = Node.new(value)
        cur.next.prev = cur
      end
    end
  end

  def printlist(cur = nil)
    if cur == nil
      cur = @head
    end
    while cur != nil
      puts cur.value
      if cur.child != nil
        puts "++++++++++"
        printlist(cur.child)
        puts "++++++++++"
      end
    cur = cur.next
    end
  end

  def flatten(cur = nil)
    if cur == nil
      cur = @head
    end
    while cur != nil
      if cur.child != nil
        temp = cur.next
        if cur.child.next != nil
          tmpr = cur.child.next
          while tmpr.next != nil
            tmpr = tmpr.next
          end
        else
          temp = cur.child
        end
        tmpr.next = temp
        temp.prev = tmpr
        cur.next = cur.child
        cur.child = nil
      end
      cur = cur.next
    end
  end

end

listone = Multileveldll.new()
listone.addnode(5)
listone.head.addchild(6)
listone.addnode(25, listone.tail.child)
listone.tail.child.next.addchild(8)
listone.addnode(6, listone.tail.child.next)
listone.tail.child.next.next.addchild(9)
listone.tail.child.next.next.child.addchild(7)
listone.addnode(33)
listone.addnode(17)
listone.addnode(2)
listone.tail.addchild(2)
listone.addnode(7, listone.tail.child)
listone.tail.child.addchild(12)
listone.addnode(5, listone.tail.child.child)
listone.tail.child.child.addchild(21)
listone.addnode(3, listone.tail.child.child.child)
listone.addnode(1)
listone.printlist()
listone.flatten()
listone.printlist()
