# ZDI-15-450: Kaseya Virtual System Administrator Authenticated Remote File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-450
- **ZDI-CAN:** ZDI-CAN-2841
- **Date:** 2015-09-23
- **CVE:** CVE-2015-6589
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Kaseya
- **Affected Products:** Virtual System Administrator
- **Credit:** Pedro Ribeiro (pedrib@gmail.com) / Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-450/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Kaseya Virtual System Administrator. Authentication is required to exploit this vulnerability. The specific flaw exists within the json.ashx HTTP handler, which does not restrict destination file paths. Attackers can leverage this vulnerability to upload and execute arbitrary code on the server under the context of IIS.

## Additional Details

Kaseya has issued an update to correct this vulnerability. More details can be found at: https://helpdesk.kaseya.com/entries/96164487--Kaseya-Security-Advisory

## Disclosure Timeline

- 2015-04-02 - Vulnerability reported to vendor
- 2015-09-23 - Coordinated public release of advisory
