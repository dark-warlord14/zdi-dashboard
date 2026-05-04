# ZDI-25-992: Adobe USD-Fileformat-plugins usdGltf Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-992
- **ZDI-CAN:** ZDI-CAN-28021
- **Date:** 2025-11-13
- **CVE:** CVE-2025-61837
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** USD-Fileformat-plugins
- **Credit:** Michael DePlante (@izobashi) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-992/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe USD-Fileformat-plugins. Interaction with the USD library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the usdGltf plugin. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/formatplugins/apsb25-114.html

## Disclosure Timeline

- 2025-08-28 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated
