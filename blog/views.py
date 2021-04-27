from django.shortcuts import render, get_object_or_404
from .models import Blog, Spy, Agent, Asset
from .forms import SpyForm, AgentForm, AssetForm
import base64

flag = False


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def terminal(request):
    if request.method == 'GET':
        return render(request, 'LOGINSPY.html')
    else:
        namee = request.POST['naam']
        idd = request.POST['num']
        # print(namee, idd)
        spies = Spy.objects.all()
        # print(spies)
        for i in spies:
            # print(i.spy_id)
            if str(i.spy_id) == str(idd):
                flag = True
                if str(i.code_name) == str(namee):
                    return render(request, 'HOMESPY.html', {'name': namee, 'f': flag})
        return render(request, 'LOGINSPY.html')


def spycraft(request):
    return render(request, 'spycraft.html', {'f': flag})


def spies(request):
    spiess = Spy.objects.all()
    return render(request, 'spies.html', {'spies': spiess, 'f': flag})


def agents(request):
    agentss = Agent.objects.all()
    return render(request, 'agents.html', {'agents': agentss, 'f': flag})


def assets(request):
    assetss = Asset.objects.all()
    return render(request, 'assets.html', {'assets': assetss, 'f': flag})


def modify(request):
    return render(request, 'modify.html')


def del_asset(request):
    return render(request, 'del_asset.html', {'assets': Asset.objects.all()})


def delete_asset(request, asset_id):
    try:
        query = Asset.objects.get(pk=asset_id)
        query.delete()
        return render(request, 'del_asset.html', {'alert_flag_t': True, 'assets': Asset.objects.all()})
    except:
        return render(request, 'del_asset.html', {'alert_flag_f': True, 'assets': Asset.objects.all()})


def del_agent(request):
    return render(request, 'del_agent.html', {'agents': Agent.objects.all()})


def delete_agent(request, agent_id):
    try:
        query = Agent.objects.get(pk=agent_id)
        query.delete()
        return render(request, 'del_agent.html', {'alert_flag_t': True, 'agents': Agent.objects.all()})
    except:
        return render(request, 'del_agent.html', {'alert_flag_f': True, 'agents': Agent.objects.all()})


def del_spy(request):
    return render(request, 'del_spy.html', {'spies': Spy.objects.all()})


def delete_spy(request, spy_id):
    try:
        query = Spy.objects.get(pk=spy_id)
        query.delete()
        return render(request, 'del_spy.html', {'alert_flag_t': True, 'spies': Spy.objects.all()})
    except:
        return render(request, 'del_spy.html', {'alert_flag_f': True, 'spies': Spy.objects.all()})


def insert_spy(request):
    return render(request, 'ispy.html')


def encode(request):
    string = request.GET.get('1ac')

    if string is None:
        string = ""

    string_bytes = string.encode('ascii')

    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')
    return render(request, 'encode.html', {'string1': string, 'string2': base64_string, 'f': flag})


def decode(request):
    base64string = request.GET.get('1ac')

    if base64string is None:
        base64string = ""

    base64string_bytes = base64string.encode("ascii")

    string_bytes = base64.b64decode(base64string_bytes)
    string = string_bytes.decode("ascii")
    return render(request, 'decode.html', {'string1': base64string, 'string2': string, 'f': flag})


def ispy(request):
    if request.method == 'POST':
        form = SpyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ispy.html', {'alert_flag_t': True})
        else:
            return render(request, 'ispy.html', {'form': form, 'alert_flag_f': True})
    else:
        form = SpyForm()
        return render(request, 'ispy.html', {'form': form})


def iagent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'iagent.html', {'alert_flag_t': True})
        else:
            return render(request, 'iagent.html', {'form': form, 'alert_flag_f': True})
    else:
        form = AgentForm()
        return render(request, 'iagent.html', {'form': form})


def iasset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'iasset.html', {'alert_flag_t': True})
        else:
            return render(request, 'iasset.html', {'form': form, 'alert_flag_f': True})
    else:
        form = AssetForm()
        return render(request, 'iasset.html', {'form': form})
