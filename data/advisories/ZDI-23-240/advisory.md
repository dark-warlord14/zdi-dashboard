# ZDI-23-240: Unity Technologies Unity Editor FBX File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-240
- **ZDI-CAN:** ZDI-CAN-18980
- **Date:** 2023-03-15
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Unity Technologies
- **Affected Products:** Unity
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Unity Technologies Unity Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FBX files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Unity Technologies has issued an update to correct this vulnerability. More details can be found at: https://unity.com/security/jan-2023-01

## Disclosure Timeline

- 2022-10-03 - Vulnerability reported to vendor
- 2023-03-15 - Coordinated public release of advisory
