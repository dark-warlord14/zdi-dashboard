# ZDI-10-129: Novell Netware Groupwise Internet Gateway Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-129
- **ZDI-CAN:** ZDI-CAN-673
- **Date:** 2010-07-16
- **CVE:** CVE-2010-2777
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** {PRL} Francis Provencher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise Internet Agent. Authentication is required to exploit this vulnerability. The flaw exists within the IMAP functionality included with GWIA. When provided with an overly long mailbox name to the CREATE verb, the IMAP server can be forced to overflow a buffer on the stack. Successful exploitation leads to remote code execution under the context of the server.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7006374&sliceId=2&docTypeID=DT_TID_1_1&dialogID=155271264&stateId=0%200%20155267598

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2010-07-16 - Coordinated public release of advisory
