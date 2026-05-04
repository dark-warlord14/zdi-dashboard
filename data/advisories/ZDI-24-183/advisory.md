# ZDI-24-183: Apache OFBiz createRegister Error Message Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-183
- **ZDI-CAN:** ZDI-CAN-23030
- **Date:** 2024-02-21
- **CVE:** CVE-2024-23946
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apache
- **Affected Products:** OFBiz
- **Credit:** Arun Shaji of Trend Micro DSLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-183/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apache OFBiz. Authentication is not required to exploit this vulnerability. The specific flaw exists within the createRegister method. The issue results from outputting an error message that includes sensitive information. An attacker can leverage this vulnerability to disclose the names of internal paths used by the system.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://issues.apache.org/jira/browse/OFBIZ-12884

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2024-02-21 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
