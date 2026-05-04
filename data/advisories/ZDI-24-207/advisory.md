# ZDI-24-207: Apple macOS VideoToolbox Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-207
- **ZDI-CAN:** ZDI-CAN-22261
- **Date:** 2024-02-26
- **CVE:** CVE-2023-42902
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must receive a malicious image file that is written to the local filesystem. The specific flaw exists within the processing of HEIC files in the VTDecoderXPCService process. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT214036

## Disclosure Timeline

- 2023-10-17 - Vulnerability reported to vendor
- 2024-02-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
