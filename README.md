Python 设计模式
===============

翻译自：[python-patterns](https://github.com/faif/python-patterns)。

Python 实现的设计模式/风格合集。

若需添加新的设计模式实现或修改已有的实现，请及时更新此文件并运行`append_output.sh`（例如：../append_output.sh borg.py）以保持底部的`OUTPUT`注释为最新版。

当前已有的设计模式：

__创建型设计模式__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [抽象工厂模式](creational/abstract_factory.py) | 将一个泛型函数和一些特定的工厂类结合使用。 |
| [borg模式](creational/borg.py) | 在实例间共享状态的单例模式。 |
| [builder](creational/builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [工厂方法](creational/factory_method.py) | 委托特定函数/方法用于创建实例。 |
| [延迟计算模式](creational/lazy_evaluation.py) | Python 中延迟计算属性。 |
| [对象池模式](creational/pool.py) | 预实例化并维护一组同类型的实例。|
| [原型模式](creational/prototype.py) | 使用工厂和克隆创建新实例（当实例化消耗较大时）。|

__结构型设计模式__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [三层架构](structural/3-tier.py) | 数据<->业务逻辑<->展示三层分离。|
| [适配器模式](structural/adapter.py) | 使用转换列表将一个接口转换为另一个。|
| [桥接模式](structural/bridge.py) | 使用客户端中间层以缓和接口变更的影响。|
| [composite](structural/composite.py) | lets clients treat individual objects and compositions uniformly |
| [装饰器模式](structural/decorator.py) | 用一个函数装饰另一个函数，以便修改输出。|
| [外观模式](structural/facade.py) | 使用一个类作为其他类的接口。|
| [享元模式](structural/flyweight.py) | 透明地恢复对象的已有实例并附带相似/相同状态。|
| [front_controller](structural/front_controller.py) | single handler requests coming to the application |
| [mvc](structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [代理模式](structural/proxy.py) | 一个将操作指向其他对象的对象。|

__行为型设计模式__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [责任链模式](behavioral/chain.py) | 提供连续的处理链以尝试处理数据 |
| [目录模式](behavioral/catalog.py) | 通用函数会根据初始化时的参数选择对应的不同方法 |
| [链式调用](behavioral/chaining_method.py) | 方法的返回值可继续调用下一个对象方法 |
| [命令模式](behavioral/command.py) | 将命令和参数打包起来供随后调用 |
| [迭代模式](behavioral/iterator.py) | 遍历一个容器并访问其中所有元素 |
| [中介者模式](behavioral/mediator.py) | 一个对象知道如何连接其他对象，行为类似于代理 |
| [备忘录模式](behavioral/memento.py) | 生成一个不透明的token可用于恢复对象到上一个状态 |
| [观察者模式](behavioral/observer.py) | 为事件/数据修改提供一个回调通知 |
| [发布/订阅模式](behavioral/publish_subscribe.py) | 将资源的事件/数据与已注册的监听者联合 |
| [注册模式](behavioral/registry.py) | 跟踪一个类的所有子类 |
| [specification](behavioral/specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](behavioral/strategy.py) | selectable operations over the same data |
| [template](behavioral/template.py) | an object imposes a structure but takes pluggable components |
| [visitor](behavioral/visitor.py) | invoke a callback for all items of a collection |

__可测试性设计模式__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [setter_injection](dft/setter_injection.py) | the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection) |

__基础模式__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [delegation_pattern](fundamental/delegation_pattern.py) | an object handles a request by delegating to a second object (the delegate) |

__其他__:

| 设计模式 | 描述 |
|:-------:| ----------- |
| [blackboard](other/blackboard.py) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](other/graph_search.py) | graphing algorithms - non gang of four pattern |
| [hsm](other/hsm/hsm.py) | hierarchical state machine - non gang of four pattern |
