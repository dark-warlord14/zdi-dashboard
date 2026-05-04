# ZDI-25-998: Adobe USD-Fileformat-plugins usdGltf Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-998
- **ZDI-CAN:** ZDI-CAN-28024
- **Date:** 2025-11-13
- **CVE:** CVE-2025-61843
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** USD-Fileformat-plugins
- **Credit:** Michael DePlante (@izobashi) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-998/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe USD-Fileformat-plugins. Interaction with the USD library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the usdGltf plugin. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/formatplugins/apsb25-114.html

## Disclosure Timeline

- 2025-09-04 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated
