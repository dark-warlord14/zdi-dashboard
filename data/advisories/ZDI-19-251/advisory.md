# ZDI-19-251: (0Day) Hewlett Packard Enterprise Intelligent Management Center FileUploadServlet Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-251
- **ZDI-CAN:** ZDI-CAN-7050
- **Date:** 2019-03-04
- **CVE:** CVE-2019-5357
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Matthias Kaiser and Steven Seeley of Incite Team (Source Incite)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of files provided to the FileUploadServlet servlet. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/24/18 – ZDI sent the vulnerability reports to the vendor 11/28/18 – The vendor replied with tracking number 01/09/19 – ZDI requested an update (for these and other related reports) 01/30/19 – The vendor PSIRT replied they were working with the engineering team to get an updated schedule 02/14/19 – ZDI notified the vendor if these are not patched that the reports will be published as 0-day on 03/04 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-10-24 - Vulnerability reported to vendor
- 2019-03-04 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
