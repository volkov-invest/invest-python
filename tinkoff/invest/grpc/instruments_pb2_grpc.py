# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import instruments_pb2 as tinkoff_dot_invest_dot_grpc_dot_instruments__pb2


class InstrumentsServiceStub(object):
    """Сервис предназначен для получения:</br>**1**. информации об инструментах;</br>**2**.
    расписания торговых сессий;</br>**3**. календаря выплат купонов по облигациям;</br>**4**.
    размера гарантийного обеспечения по фьючерсам;</br>**5**. дивидендов по ценной бумаге.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TradingSchedules = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/TradingSchedules',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesResponse.FromString,
                )
        self.BondBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/BondBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondResponse.FromString,
                )
        self.Bonds = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Bonds',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondsResponse.FromString,
                )
        self.GetBondCoupons = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetBondCoupons',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsResponse.FromString,
                )
        self.CurrencyBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/CurrencyBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrencyResponse.FromString,
                )
        self.Currencies = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Currencies',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrenciesResponse.FromString,
                )
        self.EtfBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/EtfBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfResponse.FromString,
                )
        self.Etfs = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Etfs',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfsResponse.FromString,
                )
        self.FutureBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/FutureBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FutureResponse.FromString,
                )
        self.Futures = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Futures',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FuturesResponse.FromString,
                )
        self.ShareBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/ShareBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.ShareResponse.FromString,
                )
        self.Shares = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Shares',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.SharesResponse.FromString,
                )
        self.GetAccruedInterests = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetAccruedInterests',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsResponse.FromString,
                )
        self.GetFuturesMargin = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetFuturesMargin',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginResponse.FromString,
                )
        self.GetInstrumentBy = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetInstrumentBy',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentResponse.FromString,
                )
        self.GetDividends = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetDividends',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsResponse.FromString,
                )


class InstrumentsServiceServicer(object):
    """Сервис предназначен для получения:</br>**1**. информации об инструментах;</br>**2**.
    расписания торговых сессий;</br>**3**. календаря выплат купонов по облигациям;</br>**4**.
    размера гарантийного обеспечения по фьючерсам;</br>**5**. дивидендов по ценной бумаге.
    """

    def TradingSchedules(self, request, context):
        """Метод получения расписания торгов торговых площадок.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BondBy(self, request, context):
        """Метод получения облигации по её идентификатору.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bonds(self, request, context):
        """Метод получения списка облигаций.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBondCoupons(self, request, context):
        """Метод получения графика выплат купонов по облигации
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrencyBy(self, request, context):
        """Метод получения валюты по её идентификатору.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Currencies(self, request, context):
        """Метод получения списка валют.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EtfBy(self, request, context):
        """Метод получения инвестиционного фонда по его идентификатору.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Etfs(self, request, context):
        """Метод получения списка инвестиционных фондов.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FutureBy(self, request, context):
        """Метод получения фьючерса по его идентификатору.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Futures(self, request, context):
        """Метод получения списка фьючерсов.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShareBy(self, request, context):
        """Метод получения акции по её идентификатору.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Shares(self, request, context):
        """Метод получения списка акций.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccruedInterests(self, request, context):
        """Метод получения накопленного купонного дохода по облигации.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFuturesMargin(self, request, context):
        """Метод получения размера гарантийного обеспечения по фьючерсам.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstrumentBy(self, request, context):
        """Метод получения основной информации об инструменте.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDividends(self, request, context):
        """Метод для получения событий выплаты дивидендов по инструменту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InstrumentsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TradingSchedules': grpc.unary_unary_rpc_method_handler(
                    servicer.TradingSchedules,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesResponse.SerializeToString,
            ),
            'BondBy': grpc.unary_unary_rpc_method_handler(
                    servicer.BondBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondResponse.SerializeToString,
            ),
            'Bonds': grpc.unary_unary_rpc_method_handler(
                    servicer.Bonds,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondsResponse.SerializeToString,
            ),
            'GetBondCoupons': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBondCoupons,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsResponse.SerializeToString,
            ),
            'CurrencyBy': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrencyBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrencyResponse.SerializeToString,
            ),
            'Currencies': grpc.unary_unary_rpc_method_handler(
                    servicer.Currencies,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrenciesResponse.SerializeToString,
            ),
            'EtfBy': grpc.unary_unary_rpc_method_handler(
                    servicer.EtfBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfResponse.SerializeToString,
            ),
            'Etfs': grpc.unary_unary_rpc_method_handler(
                    servicer.Etfs,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfsResponse.SerializeToString,
            ),
            'FutureBy': grpc.unary_unary_rpc_method_handler(
                    servicer.FutureBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FutureResponse.SerializeToString,
            ),
            'Futures': grpc.unary_unary_rpc_method_handler(
                    servicer.Futures,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FuturesResponse.SerializeToString,
            ),
            'ShareBy': grpc.unary_unary_rpc_method_handler(
                    servicer.ShareBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.ShareResponse.SerializeToString,
            ),
            'Shares': grpc.unary_unary_rpc_method_handler(
                    servicer.Shares,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.SharesResponse.SerializeToString,
            ),
            'GetAccruedInterests': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccruedInterests,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsResponse.SerializeToString,
            ),
            'GetFuturesMargin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFuturesMargin,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginResponse.SerializeToString,
            ),
            'GetInstrumentBy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstrumentBy,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentResponse.SerializeToString,
            ),
            'GetDividends': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDividends,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.InstrumentsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InstrumentsService(object):
    """Сервис предназначен для получения:</br>**1**. информации об инструментах;</br>**2**.
    расписания торговых сессий;</br>**3**. календаря выплат купонов по облигациям;</br>**4**.
    размера гарантийного обеспечения по фьючерсам;</br>**5**. дивидендов по ценной бумаге.
    """

    @staticmethod
    def TradingSchedules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/TradingSchedules',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.TradingSchedulesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BondBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/BondBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bonds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Bonds',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.BondsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBondCoupons(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetBondCoupons',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetBondCouponsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrencyBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/CurrencyBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrencyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Currencies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Currencies',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.CurrenciesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EtfBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/EtfBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Etfs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Etfs',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.EtfsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FutureBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/FutureBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FutureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Futures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Futures',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.FuturesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShareBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/ShareBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.ShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Shares(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/Shares',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.SharesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccruedInterests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetAccruedInterests',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetAccruedInterestsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFuturesMargin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetFuturesMargin',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetFuturesMarginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstrumentBy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetInstrumentBy',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.InstrumentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDividends(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetDividends',
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_instruments__pb2.GetDividendsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
