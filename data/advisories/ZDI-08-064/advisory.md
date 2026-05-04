# ZDI-08-064: Novell eDirectory dhost.exe Accept Language Header Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-064
- **ZDI-CAN:** ZDI-CAN-313
- **Date:** 2008-10-08
- **CVE:** CVE-2008-4479
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-064/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Authentication is not required to exploit this vulnerability. The specific flaw resides in the web console running on TCP ports 8028 and 8030. The server exposes a web interface and accepts SOAP connections. The service copies the contents of the Accept-Language header within a SOAP request into a fixed-length buffer without any bounds checking. If an attacker sends a specially crafted request it will trigger an overflow during a memory copy operation leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7000086&sliceId=1&docTypeID=DT_TID_1_1&dialogID=78066829&stateId=0%200%2078062953

## Disclosure Timeline

- 2008-04-08 - Vulnerability reported to vendor
- 2008-10-08 - Coordinated public release of advisory
