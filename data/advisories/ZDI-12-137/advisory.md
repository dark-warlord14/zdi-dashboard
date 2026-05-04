# ZDI-12-137: Apple Mac OS X libsecurity_cdsa_plugin Malloc Integer Truncation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-137
- **ZDI-CAN:** ZDI-CAN-1386
- **Date:** 2012-08-17
- **CVE:** CVE-2012-0662
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** aazubel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-137/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Mac OSX. Authentication is not required to exploit this vulnerability. The flaw exists within the libsecurity_cdsa_plugin which implements routines defined in libsecurity_cssm. The library defines an allocation routine as having an argument type uint32. The implemented methods in the cdsa_plugin accept parameter having type size_t, this value is truncated from 64 bits to 32 bits when being passed to the library routine. This can lead to an underallocated memory region and ultimately a write out of bounds. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
