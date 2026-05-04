# ZDI-11-089: Novell ZenWorks TFTPD Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-089
- **ZDI-CAN:** ZDI-CAN-877
- **Date:** 2011-02-17
- **CVE:** CVE-2010-4323
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Francis Provencher for Protek Researchh Lab's AbdulAziz Hariri of ThirdEyeTesters SilentSignal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks Configuration Manager. Authentication is not required to exploit this vulnerability. The flaw exists within the novell-tftp.exe component which listens by default on UDP port 69. When handling a request the process blindly copies user supplied data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the ZenWorks user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7007896&sliceId=2&docTypeID=DT_TID_1_1&dialogID=205671351&stateId=0%200%20205669596

## Disclosure Timeline

- 2010-08-23 - Vulnerability reported to vendor
- 2011-02-17 - Coordinated public release of advisory
