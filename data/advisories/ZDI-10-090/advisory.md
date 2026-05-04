# ZDI-10-090: Novell ZENworks Configuration Management Preboot Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-090
- **ZDI-CAN:** ZDI-CAN-679
- **Date:** 2010-06-01
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Preboot Service (novell-pbserv.exe). This service listens for incoming connections on TCP port 998. The service uses a simple binary protocol where the first DWORD is an opcode followed by the specific opcode's data, typically in length/value pairs. These length values are not checked against the destination buffers size allowing for stack-based overflows to occur. This can lead to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7005572&sliceId=1&docTypeID=DT_TID_1_1&dialogID=138523325&stateId=0%200%20138517923

## Disclosure Timeline

- 2010-02-09 - Vulnerability reported to vendor
- 2010-06-01 - Coordinated public release of advisory
