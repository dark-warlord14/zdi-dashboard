# ZDI-23-1030: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Workspace Unrestricted Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1030
- **ZDI-CAN:** ZDI-CAN-20536
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39462
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1030/
## Vulnerability Details

This vulnerability allows remote attackers to upload arbitrary files on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of workspace files. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilitites to execute arbitrary code in the context of root.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
