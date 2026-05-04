# ZDI-24-1698: libarchive run_filters Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1698
- **ZDI-CAN:** ZDI-CAN-23999
- **Date:** 2024-12-19
- **CVE:** CVE-2024-26256
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** libarchive
- **Affected Products:** libarchive
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1698/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of libarchive. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the run_filters method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

libarchive has issued an update to correct this vulnerability. More details can be found at: https://github.com/libarchive/libarchive/pull/2269

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
