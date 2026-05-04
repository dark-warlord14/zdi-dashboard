# ZDI-10-145: Novell ZENWorks Remote Management Agent Weak Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-145
- **ZDI-CAN:** ZDI-CAN-750
- **Date:** 2010-08-09
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** sb
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks Remote Management. Access to a single node with Remote Management client installed and configured is required. The specific flaw exists within the storage of Remote Management authentication information on the client. The client utilizes a password stored in the registry that is common among all nodes. This can be exploited by an attacker to execute remote code on any target with the client installed.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=7006557&sliceId=1&docTypeID=DT_TID_1_1&dialogID=80488553&stateId=1%200%2080486291

## Disclosure Timeline

- 2010-06-07 - Vulnerability reported to vendor
- 2010-08-09 - Coordinated public release of advisory
