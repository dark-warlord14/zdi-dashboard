# ZDI-25-318: Hewlett Packard Enterprise StoreOnce VSA getServerPayload Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-318
- **ZDI-CAN:** ZDI-CAN-25315
- **Date:** 2025-06-02
- **CVE:** CVE-2025-37095
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** StoreOnce VSA
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-318/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise StoreOnce VSA. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the getServerPayload method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
