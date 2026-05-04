# ZDI-12-196: Novell Groupwise GWIA ber_get_stringa Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-196
- **ZDI-CAN:** ZDI-CAN-1347
- **Date:** 2012-12-21
- **CVE:** CVE-2012-0417
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Francis Provencher From Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-196/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise. Authentication is not required to exploit this vulnerability. The flaw exists within the Groupwise Internet Agent component, specifically the optional LDAP server which listens on tcp port 389. When parsing a BER encoded parameter the specified size is used to allocate a destination buffer. A properly encoded BER chunk could cause an integer size value to wrap before buffer allocation. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM account.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7010770

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
