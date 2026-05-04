# ZDI-11-111: (0Day) Hewlett-Packard Virtual SAN Appliance hydra.exe Login Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-111
- **ZDI-CAN:** ZDI-CAN-906
- **Date:** 2011-03-23
- **CVE:** CVE-2011-4147
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Virtual SAN Appliance
- **Credit:** Nicolas Gregoire of Agarri (www.agarri.fr)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-111/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Virtual SAN appliance. Authentication is not required to exploit this vulnerability. The flaw exists within the hydra.exe component which listens by default on port 13838. When parsing a login request the Hydra daemon will call sscanf() using fixed-length stack buffers and no length checks. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM service.

## Additional Details

March 23, 2011 - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigations: This vulnerability could be mitigated by administrators by restricting communication with the hydra agent to known client IP addresses.

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2011-03-23 - Coordinated public release of advisory
