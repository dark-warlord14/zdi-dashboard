# ZDI-25-581: (Pwn2Own) Microsoft SharePoint DataSetSurrogateSelector Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-581
- **ZDI-CAN:** ZDI-CAN-27247
- **Date:** 2025-07-08
- **CVE:** CVE-2025-49704
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-581/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the DataSetSurrogateSelector class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint web server process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49704

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
