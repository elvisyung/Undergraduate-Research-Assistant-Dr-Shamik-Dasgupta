# Histogram (Colored) # 2
# def drawcolouredhist2(xc, yc):
    #graph13 = plt.figure()
    
    #cseries=pd.Series([1/len(xc)]*len(xc))
    #colormap = mpl.cm.gist_rainbow
    #mpl.pyplot.hexbin(xc, yc, gridsize=(hexbinnum), C=cseries, reduce_C_function=np.sum,  cmap=colormap, extent= (-asize, asize, -asize, asize))
    
    #plt.colorbar(orientation='vertical', label="Fraction of Time Fly Spent in Area")
    #plt.axis([-asize, asize, -asize, asize])
    #plt.xticks([-asize, -4*asize/5, -3*asize/5, -2*asize/5, -asize/5, 0, asize/5, 2*asize/5, 3*asize/5, 4*asize/5, asize])
    #plt.yticks([-asize, -4*asize/5, -3*asize/5, -2*asize/5, -asize/5, 0, asize/5, 2*asize/5, 3*asize/5, 4*asize/5, asize])
    #plt.gca().set_aspect('equal', adjustable='box')
    #plt.xlabel('x position (cm)')
    #plt.ylabel('y position (cm)')
    
    #if arena==1:
        #plt.title('Fly Position Frequency Blank Arena')
        #plt.suptitle(str(name))
    #if arena==2:
        #drawcircle(graph13, centcircr)
        #drawcircle(graph13, centcircl)
        #plt.title('Fly Position Frequency Side Objects Arena')
        #plt.suptitle(str(name))
    #if arena==3:
        #drawcircle(graph13, centcirct)
        #drawcircle(graph13, centcircb)
        #plt.title('Fly Position Frequency Top/ Bottom Objects Arena')
        #plt.suptitle(str(name))
    #if arena==4:
        #drawcircle(graph13, centcirctr)
        #drawcircle(graph13, centcirctl)
        #drawcircle(graph13, centcircbr)
        #drawcircle(graph13, centcircbl)
        #plt.title('Fly Position Frequency 4 Objects Arena')
        #plt.suptitle(str(name))
    #if arena==5:
        #drawcircle(graph13, centcircr)
        #plt.title('Fly Position Frequency Right Object Arena')
        #plt.suptitle(str(name))
    #if arena==6:
        #drawcircle(graph13, centcircl)
        #plt.title('Fly Position Frequency Left Object Arena')
        #plt.suptitle(str(name))
    #if arena==7:
        #drawcircle(graph13, centcirc1)
        #drawcircle(graph13, centcirc2)
        #drawcircle(graph13, centcirc3)
        #drawcircle(graph13, centcirc4)
        #plt.title('Fly Position Frequency Custom Objects Arena')
        #plt.suptitle(str(name))

# Quiver Plot
# def drawquiv(xq, yq, dxq, dyq, utimeq, time):
    #norm = mpl.colors.Normalize()
    #qcolormap = mpl.cm.gist_rainbow
    #cbnorm = mpl.colors.Normalize(vmin=0, vmax=time)
    
    #graph1 = plt.figure()
    #plt.axis([-asize, asize, -asize, asize])
    #plt.xlabel('x position (cm)')
    #plt.ylabel('y position (cm)')
    #plt.xticks([-asize, -4*asize/5, -3*asize/5, -2*asize/5, -asize/5, 0, asize/5, 2*asize/5, 3*asize/5, 4*asize/5, asize])
    #plt.yticks([-asize, -4*asize/5, -3*asize/5, -2*asize/5, -asize/5, 0, asize/5, 2*asize/5, 3*asize/5, 4*asize/5, asize])
   
    #if (quivall==1):
        #plt.quiver(xq, yq, dxq, dyq, units="x", minlength=0.0000000000001)

    #else:
        #plt.quiver(xq, yq, dxq, dyq, units="x", minlength=0.0000000000001, color=qcolormap(norm(utimeq)))
        #plt.colorbar(mpl.cm.ScalarMappable(norm=cbnorm, cmap=qcolormap), orientation='vertical', label="Time (minutes)")
        #plt.plot(xq,yq)
        
    #plt.gca().set_aspect('equal', adjustable='box')

    
    #if arena==1:
        #plt.title('Fly Position Blank Arena')
        #plt.suptitle(str(name))
    #if arena==2:
        #drawcircle(graph1, centcircr)
        #drawcircle(graph1, centcircl)
        #plt.title('Fly Position Side Objects Arena' )
        #plt.suptitle(str(name))
    #if arena==3:
        #drawcircle(graph1, centcirct)
        #drawcircle(graph1, centcircb)
        #plt.title('Fly Position Top/ Bottom Objects Arena')
        #plt.suptitle(str(name))
    #if arena==4:
        #drawcircle(graph1, centcirctr)
        #drawcircle(graph1, centcirctl)
        #drawcircle(graph1, centcircbr)
        #drawcircle(graph1, centcircbl)
        #plt.title('Fly Position 4 Objects Arena')
        #plt.suptitle(str(name))
    #if arena==5:
        #drawcircle(graph1, centcircr)
        #plt.title('Fly Position Right Object Arena')
        #plt.suptitle(str(name))
    #if arena==6:
        #drawcircle(graph1, centcircl)
        #plt.title('Fly Position Left Object Arena')
        #plt.suptitle(str(name))
    #if arena==7:
        #drawcircle(graph1, centcirc1)
        #drawcircle(graph1, centcirc2)
        #drawcircle(graph1, centcirc3)
        #drawcircle(graph1, centcirc4)
        #plt.title('Fly Position Custom Objects Arena')
        #plt.suptitle(str(name))
    #plt.show()