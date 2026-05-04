# ZDI-10-169: Novell Netware SSHD.NLM Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-169
- **ZDI-CAN:** ZDI-CAN-674
- **Date:** 2010-09-01
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Francis Provencher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-169/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware. Authentication is required to exploit this vulnerability. The flaw exists within SSHD.NLM. When the application attempts to resolve an absolute path on the server, a 512 byte destination buffer is used without bounds checking. By providing a large enough value, an attacker can cause a buffer to be overflowed. Successful exploitation results in remote code execution under the context of the server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7006756&sliceId=1&docTypeID=DT_TID_1_1&dialogID=164386838&stateId=0%200%20164390561

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2010-09-01 - Coordinated public release of advisory
