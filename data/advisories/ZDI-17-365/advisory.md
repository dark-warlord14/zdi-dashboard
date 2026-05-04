# ZDI-17-365: Hewlett Packard Enterprise Cloud Optimizer DownloadServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-365
- **ZDI-CAN:** ZDI-CAN-4221
- **Date:** 2017-05-18
- **CVE:** CVE-2017-8944
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Cloud Optimizer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-365/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Hewlett Packard Enterprise Cloud Optimizer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DownloadServlet servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03748en_us

## Disclosure Timeline

- 2016-12-28 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
