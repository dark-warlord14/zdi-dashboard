# ZDI-09-046: Novell Privileged User Manager Remote DLL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-046
- **ZDI-CAN:** ZDI-CAN-493
- **Date:** 2009-07-21
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Privileged User Manager
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems running vulnerable versions of Novell's Privileged User Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the unifid.exe service which binds on port 29010 for a protocol providing RPC-like functionality encapsulated over SSL. This protocol allows a client to make a method call into a module. The 'spf' RPC call is implemented unsafely allowing remote attackers to load arbitrary modules over the network resulting in code execution under the context of the service.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7003640&sliceId=1&docTypeID=DT_TID_1_1&dialogID=72895793&stateId=0%200%2072897343

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-07-21 - Coordinated public release of advisory
