# ZDI-11-345: TrendMicro Control Manager CmdProcessor.exe AddTask Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-345
- **ZDI-CAN:** ZDI-CAN-1138
- **Date:** 2011-12-07
- **CVE:** N/A
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-345/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trent Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within CmdProcessor.exe service running on TCP port 20101. The vulnerable function is the CGenericScheduler::AddTask function of cmdHandlerRedAlertController.dll. When processing a specially crafted IPC packet, controlled data is copied into a 256-byte stack buffer. This can be exploited to execute remote code under the context of the user

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://downloadcenter.trendmicro.com/index.php?prodid=7

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-12-07 - Coordinated public release of advisory
