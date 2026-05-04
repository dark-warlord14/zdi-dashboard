# ZDI-15-153: Novell ZENworks Preboot Policy Service Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-153
- **ZDI-CAN:** ZDI-CAN-2491
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0786
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-153/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks. Authentication is not required to exploit this vulnerability. The specific flaw exists within ZENworks Preboot Policy Service, which listens on port 13331. The vulnerability is in the logging functionality, which copies attacker provided data into a fixed size stack buffer. An attacker could leverage this to execute arbitrary code as the local user __z_0_1__, which has Administrator privileges.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2014-09-11 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
