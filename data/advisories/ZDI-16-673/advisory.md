# ZDI-16-673: Mozilla Firefox ClearKeyDecryptor Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-673
- **ZDI-CAN:** ZDI-CAN-3766
- **Date:** 2016-12-19
- **CVE:** CVE-2016-2837
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-673/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ClearKey encrypted media. The issue lies in the failure to validate the length of encrypted data prior to copying into a heap-based buffer. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2016-77/

## Disclosure Timeline

- 2016-05-20 - Vulnerability reported to vendor
- 2016-12-19 - Coordinated public release of advisory
