# ZDI-15-149: Novell Zenworks Rtrlet.class Session ID Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-149
- **ZDI-CAN:** ZDI-CAN-2579
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0784
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-149/
## Vulnerability Details

This vulnerability allows attackers to disclose Session ID's of logged in users on vulnerable installations of Novell Zenworks. User interaction is not required to exploit this vulnerability. The specific flaw exists within Rtrlet.class. By sending a POST request with the maintenance variable set to "ShowLogins" the applet returns information about the logged in users. An attacker can leverage this to leak the Session ID's of the logged in users.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2015-01-15 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
