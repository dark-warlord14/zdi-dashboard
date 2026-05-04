# ZDI-11-235: TrendMicro Control Manager CASProcessor.exe BLOB Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-235
- **ZDI-CAN:** ZDI-CAN-1139
- **Date:** 2011-07-12
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-235/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within En_Utility.dll. A module called from CASProcessor.exe running on TCP port 20801. A specially crafted packet with malformed BLOB encrypted data, is handled by HandleMcpRequest(), and contains instructions that will allow for an integer wrap, leading to a heap overflow. An attacker can leverage this vulnerability to execute arbitrary code under the context of the SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-us/1058292.aspx

## Disclosure Timeline

- 2011-04-07 - Vulnerability reported to vendor
- 2011-07-12 - Coordinated public release of advisory
