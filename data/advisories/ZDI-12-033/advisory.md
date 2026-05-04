# ZDI-12-033: ABB WebWare RobNetScanHost.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-033
- **ZDI-CAN:** ZDI-CAN-1260
- **Date:** 2012-02-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ABB
- **Affected Products:** WebWare
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB WebWare. Authentication is not required to exploit this vulnerability. The specific flaw exists within RobNetScanHost.exe and its parsing of network packets accepted on port 5512. The parsing of 'Netscan' packets with opcodes 0xE and 0xA are vulnerable to a stack-based buffer overflow with a fixed allocation of 20 bytes. This vulnerability can be exploited to execute arbitrary code in the context of the service process (LocalSystem).

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: http://www05.abb.com/global/scot/scot348.nsf/veritydisplay/f261be074480dc24c12579a00049ecd5/$file/si10227a1%20vulnerability%20security%20advisory.pdf

## Disclosure Timeline

- 2011-10-10 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
