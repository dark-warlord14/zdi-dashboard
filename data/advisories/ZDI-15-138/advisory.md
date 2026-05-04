# ZDI-15-138: ManageEngine NetFlow Analyzer CReportPDFServlet schFilePath Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-138
- **ZDI-CAN:** ZDI-CAN-2429
- **Date:** 2015-04-15
- **CVE:** CVE-2014-5445
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** ManageEngine
- **Affected Products:** NetFlow Analyzer
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-138/
## Vulnerability Details

This vulnerability allows remote attackers to disclose files on vulnerable installations of ManageEngine NetFlow Analyzer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of input to the CReportPDFServlet servlet. The issue lies in the failure to perform any validation of the input filename. A remote attacker can exploit this vulnerability to disclose files from the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://support.zoho.com/portal/manageengine/helpcenter/articles/cve-2014-5445-cve-2014-5446-fix-for-arbitrary-file-download

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
