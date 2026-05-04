# ZDI-11-171: Sybase OneBridge Mobile Data Suite Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-171
- **ZDI-CAN:** ZDI-CAN-1068
- **Date:** 2011-06-03
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** OneBridge
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase OneBridge Mobile Data Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the iMailGatewayService server process (ECTrace.dll) which listens for encrypted requests by default on TCP port 993 (IMAP) and port 587 (SMTP). The process fails to properly sanitize malformed user string inputs before passing to the authentication logging function. By providing a specially crafted string with format specifiers this can be leveraged to trigger a format string vulnerability which can lead to arbitrary code execution in the context of the server process.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1092074

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-03 - Coordinated public release of advisory
