# ZDI-22-1595: Microsoft Exchange Autodiscover Server-Side Request Forgery Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1595
- **ZDI-CAN:** ZDI-CAN-18802
- **Date:** 2022-10-17
- **CVE:** CVE-2022-41040
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** DA-0x43-Dx4-DA-Hx2-Tx2-TP-S-Q from GTSC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1595/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the Autodiscover service. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040

## Disclosure Timeline

- 2022-09-09 - Vulnerability reported to vendor
- 2022-10-17 - Coordinated public release of advisory
- 2022-11-18 - Advisory Updated
