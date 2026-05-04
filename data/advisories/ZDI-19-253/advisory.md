# ZDI-19-253: (Pwn2Own) Samsung Galaxy S9 ASN.1 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-253
- **ZDI-CAN:** ZDI-CAN-7472
- **Date:** 2019-03-05
- **CVE:** CVE-2019-6740
- **CVSS:** 9.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S9
- **Credit:** fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Galaxy S9. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ASN.1 parser. When parsing ASN.1 strings, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in January 2019 Security Update (SMR-JAN-2019 - SVE-2018-13467)

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-03-05 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
