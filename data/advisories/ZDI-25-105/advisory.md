# ZDI-25-105: NI DAQExpress LVPROJECT File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-105
- **ZDI-CAN:** ZDI-CAN-21908
- **Date:** 2025-03-03
- **CVE:** CVE-2024-12741
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** DAQExpress
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-105/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI DAQExpress. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LVPROJECT files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/deserialization-of-untrusted-data-vulnerability-in-ni-daqexpress.html

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated
