# ZDI-15-449: Kaseya Virtual System Administrator Remote File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-449
- **ZDI-CAN:** ZDI-CAN-2840
- **Date:** 2015-09-23
- **CVE:** CVE-2015-6922
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Kaseya
- **Affected Products:** Virtual System Administrator
- **Credit:** Pedro Ribeiro (pedrib@gmail.com) / Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-449/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Kaseya Virtual System Administrator. Authentication is not required to exploit this vulnerability. The specific flaw exists within the uploader.aspx page, which does not properly require that users be authenticated and does not restrict destination file paths. Attackers can leverage this vulnerability to upload and execute arbitrary code on the server under the context of IIS.

## Additional Details

Kaseya has issued an update to correct this vulnerability. More details can be found at: https://helpdesk.kaseya.com/entries/96164487--Kaseya-Security-Advisory

## Disclosure Timeline

- 2015-04-02 - Vulnerability reported to vendor
- 2015-09-23 - Coordinated public release of advisory
