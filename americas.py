# import pygal
import pygal.maps.world

# wm = pygal.Worldmap()
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America',['ca','mx','us']) # .add(label,list)
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf',
                        'gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg') # Write the chart in the specified file