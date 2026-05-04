# ZDI-10-188: IBM Tivoli Storage Manager FastBack Mount NULL Pointer Dereference DoS Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-188
- **ZDI-CAN:** ZDI-CAN-701
- **Date:** 2010-09-30
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager FastBack
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-188/
## Vulnerability Details

This vulnerability allows remote attackers to deny service to clients on vulnerable installations of IBM Tivoli FastBack Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FastBackMount.exe component which listens by default on TCP port 30051. When handling a failed memory allocation due to a large size provided by an attacker an exception handler is invoked which attempts to log the event. Due to the previously failed allocation a null pointer is dereferenced when creating a string to send to log causing the process to terminate. A remote attacker can exploit this vulnerability to terminate the FastBackMount.exe process and deny service to clients.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 4

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-09-30 - Coordinated public release of advisory
