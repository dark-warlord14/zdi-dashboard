# ZDI-15-152: Novell Zenworks com.novell.zenworks.inventory.rtr.actionclasses.wcreports Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-152
- **ZDI-CAN:** ZDI-CAN-2578
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0785
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-152/
## Vulnerability Details

This vulnerability allows attackers to obtain sensitive information on vulnerable installations of Novell Zenworks. User interaction is not required to exploit this vulnerability. The specific flaw exists within com.novell.zenworks.inventory.rtr.actionclasses.wcreports. The issue lies in the failure to sanitize the path of the "dirname" variable. The attacker can leverage this to disclose the contents of folders on the system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2015-01-15 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
