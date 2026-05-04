# ZDI-25-833: NVIDIA Transformers4Rec load_model_trainer_states_from_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-833
- **ZDI-CAN:** ZDI-CAN-27199
- **Date:** 2025-08-14
- **CVE:** CVE-2025-23298
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Transformers4Rec
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-833/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NVIDIA Transformers4Rec. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the load_model_trainer_states_from_checkpoint function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5683

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-08-14 - Coordinated public release of advisory
- 2025-09-26 - Advisory Updated
